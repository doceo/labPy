
import cv2
import numpy as np
from datetime import datetime

class DogTracker:
    def __init__(self):
        self.positions = []
        self.tracking = False
        
    def run(self):
        # Initialize video capture (0 for default camera)
        cap = cv2.VideoCapture(0)
        
        # Create tracker
        tracker = cv2.legacy.TrackerCSRT_create()
        
        # Initialize tracking window
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture video")
            return
            
        # Let user select ROI (Region of Interest) around the dog
        bbox = cv2.selectROI("Select Dog", frame, False)
        tracker.init(frame, bbox)
        cv2.destroyWindow("Select Dog")
        
        # Trail visualization
        trail = np.zeros_like(frame)
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            # Update tracker
            success, bbox = tracker.update(frame)
            
            if success:
                # Draw bounding box
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, p1, p2, (0, 255, 0), 2)
                
                # Record position
                center = (int(bbox[0] + bbox[2]/2), int(bbox[1] + bbox[3]/2))
                self.positions.append(center)
                
                # Draw trail
                if len(self.positions) > 1:
                    for i in range(1, len(self.positions)):
                        cv2.line(trail, self.positions[i-1], self.positions[i], 
                                (0, 0, 255), 2)
                
                # Combine frame and trail
                combined = cv2.addWeighted(frame, 1.0, trail, 0.3, 0.0)
                
                # Display info
                cv2.putText(combined, "Tracking", (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Lost", (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                
            # Show frame
            cv2.imshow("Dog Tracking", combined if success else frame)
            
            # Exit on 'q' press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    tracker = DogTracker()
    tracker.run()
