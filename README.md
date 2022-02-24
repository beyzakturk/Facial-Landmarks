# Facial Landmarks

Face landmark detection is a computer vision task where we want to detect and track keypoints from a human face. This task applies to many problems.

For example, we can use the keypoints for detecting a human’s head pose position and rotation. With that, we can track whether a driver is paying attention or not. Also, we can use the keypoints for applying an augmented reality easier. And there are so many solutions that we can generate based on this task.

![Image ](https://929687.smushcdn.com/2633864/wp-content/uploads/2017/04/facial_landmarks_dlib_example.jpg?lossy=1&strip=1&webp=1)

## What is Dlib?
It‘s a landmark’s facial detector with pre-trained models, the dlib is used to estimate the location of 68 coordinates (x, y) that map the facial points on a person’s face like image below.

![Image ](https://929687.smushcdn.com/2633864/wp-content/uploads/2017/04/facial_landmarks_68markup-768x619.jpg?lossy=1&strip=1&webp=1)

These points are identified from the pre-trained model where the [iBUG300-W](https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/) dataset was used.

The facial landmark detector included in the dlib library is an implementation of the [One Millisecond Face Alignment with an Ensemble of Regression Trees](https://www.semanticscholar.org/paper/One-millisecond-face-alignment-with-an-ensemble-of-Kazemi-Sullivan/d78b6a5b0dcaa81b1faea5fb0000045a62513567?p2df) paper by Kazemi and Sullivan (2014).

This method starts by using:
- A training set of labeled facial landmarks on an image. These images are manually labeled, specifying specific (x, y)-coordinates of regions surrounding each facial structure.
- Priors, of more specifically, the probability on distance between pairs of input pixels.

Given this training data, an ensemble of regression trees are trained to estimate the facial landmark positions directly from the pixel intensities themselves (i.e., no “feature extraction” is taking place).

The end result is a facial landmark detector that can be used to detect facial landmarks in real-time with high quality predictions.

For more information and details on this specific technique, be sure to read the paper by Kazemi and Sullivan linked to above, along with the official dlib announcement.

![Image ](https://929687.smushcdn.com/2633864/wp-content/uploads/2017/04/facial_landmarks_example_02_result.jpg?lossy=1&strip=1&webp=1)
