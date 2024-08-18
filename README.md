# Lane-Departure-Warning-System
A lane departure warning system alerts drivers when their car unintentionally drifts out of its lane without proper signaling, helping to prevent accidents by making drowsy or distracted drivers aware of their situation.


#### **Project Title**: Lane Departure Warning System (LDWS)

#### **Project Overview**:
The Lane Departure Warning System (LDWS) is a crucial component of Advanced Driver Assistance Systems (ADAS). This system is designed to enhance vehicle safety by providing alerts to drivers when they unintentionally drift out of their lane. It plays a significant role in reducing accidents caused by driver inattention or drowsiness, thereby contributing to safer roadways.

---

### **1. Theory**

#### **1.1 Advanced Driver Assistance System (ADAS)**
ADAS is a collection of electronic systems that aid the driver in the driving process. The goal of these systems is to increase vehicle safety and provide an overall more comfortable driving experience. ADAS includes several key components:

- **Adaptive Cruise Control (ACC)**: Maintains a safe distance from the vehicle ahead by automatically adjusting the speed.
- **Lane Departure Warning System (LDWS)**: Alerts the driver if the vehicle unintentionally drifts out of its lane.
- **Forward Collision Warning (FCW)**: Warns the driver of an impending collision with a vehicle or object in front.
- **Automatic Emergency Braking (AEB)**: Automatically applies the brakes to prevent or mitigate a collision.
- **Blind Spot Detection (BSD)**: Monitors areas around the vehicle that are not visible to the driver and alerts them to potential hazards.
- **Parking Assistance System (PAS)**: Assists the driver in parking by providing guidance or taking control of the vehicle during the parking process.
- **Traffic Sign Recognition (TSR)**: Detects and interprets road signs to provide information to the driver.

#### **1.2 Advantages of ADAS**
1. **Safety**: Enhances overall vehicle safety by preventing accidents.
2. **Collision Mitigation**: Reduces the severity of collisions.
3. **Driver Assistance**: Helps drivers in various driving tasks.
4. **Driver Convenience**: Makes driving more comfortable and less stressful.
5. **Economic Fuel Consumption**: Potentially improves fuel efficiency.

#### **1.3 Disadvantages of ADAS**
1. **Over-Reliance**: Drivers may become too dependent on these systems.
2. **Cost**: ADAS can be expensive to install and maintain.
3. **Potential Learning Curve**: Drivers may need time to learn how to use these systems effectively.
4. **False Alarms**: The system may occasionally provide unnecessary warnings.
5. **Performance in Certain Conditions**: ADAS may not perform well in specific weather or road conditions.

---

### **2. Lane Departure Warning System (LDWS)**

#### **2.1 Advantages of LDWS**
1. **Safety**: Provides early warnings to prevent unintended lane departures.
2. **Driver Assistance**: Helps the driver maintain lane discipline.
3. **Early Warning System**: Alerts the driver well in advance of potential danger.
4. **Flexibility and Customization**: Can be tailored to suit different driving styles and preferences.

#### **2.2 Disadvantages of LDWS**
1. **Cost**: Installation and maintenance can be expensive.
2. **Over-Reliance**: Drivers might become too dependent on the system.
3. **False Alarms**: The system may issue unnecessary warnings.
4. **Performance in Certain Conditions**: May not work effectively in adverse weather or road conditions.

---

### **3. Process Overview**

#### **3.1 Image Acquisition**
- Capturing images from the environment using a camera mounted on the vehicle.

#### **3.2 Image Preprocessing**
- **Image Enhancement**: Improving the quality of the captured image.
- **Image Resizing**: Adjusting the image size for further processing.
- **Image Normalization**: Standardizing the image to a specific range of values.
- **Image Compression**: Reducing the size of the image file for faster processing.

#### **3.3 Edge Detection**
- **Step 1: Grayscale Conversion**: Converting the image to grayscale.
- **Step 2: Noise Reduction**: Reducing unwanted noise in the image.
- **Step 3: Gradient Calculation**: Calculating the gradient to highlight edges.
- **Step 4: Non-Maxima Suppression**: Thinning the edges to create a crisp outline.
- **Step 5: Double Thresholding**: Classifying edges based on their intensity.
- **Step 6: Edge Tracking with Hysteresis**: Finalizing the edges by connecting strong edges and suppressing weak ones.

#### **3.4 Hough Transform**
- **Step 1: Conversion into Hough Space**: Transforming the image to identify potential lines.
- **Step 2: Voting**: Accumulating evidence for lines by voting.
- **Step 3: Accumulator Thresholding**: Identifying the most likely lines based on votes.
- **Step 4: Line Extraction**: Extracting the detected lines from the image.
- **Step 5: Post Processing**: Merging, filtering, and extrapolating lines to refine the detection.

#### **3.5 Kalman Filter**
- **State Prediction**: Estimating the future position of detected lines.
- **Measurement Fusion**: Combining data from multiple sources for accurate tracking.
- **Smoothing and Filtering**: Reducing noise and ensuring smooth detection.
- **Prediction of State**: Continuously predicting the state of the lane markers.
- **Error Correction**: Adjusting predictions to minimize errors.

#### **3.6 Euclidean Distance Calculation**
- Calculating the distance between the vehicle's current position and the lane markers.
- Comparing the distance to a predefined threshold to determine if the vehicle is drifting out of the lane.
- Triggering warnings if the threshold is exceeded.


