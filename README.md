# Histogram and Adaptive Histogram Equalization for a daylight scene

## Objective

Histogram Equalization is an image processing technique that adjusts the contrast of an
image. The aim of this project is to enhance the image contrast of a dataset using two techniques.

* Histogram Equalization
* Adaptive Histogram Equalization

The challenge is to not use any inbuilt functions from open source libraries but to implement the mathematics behind the functions and understand how things work behind the API. Once you have implemented both of them compare the result of each technique and validate them with the original dataset.

## Contents

```
├───LICENSE
├───proj2_part1_report.pdf
├───README.md
├───Hist_and_Clahe.py
├───hist_data
└───outputs

```

## Requirements

- OpenCV `pip install opencv-python`
- Numpy `pip install numpy`
- glob `pip install glob2`
- Download and install Anaconda {easy}

## Instructions to run

1. Clone the repository

   ```
   git clone 
   ```
2. Open the folder in the IDE
3. Run the `Hist_and_Clahe.py` file

   ```
   python Hist_and_Clahe.py
   ```
4. Uncomment the commented lines at the end to save outputs to outputs folder

## Results

### Comparison of Histogram Equalization and Adaptive Histogram Equalization

<p align="center">
  <img width="500" height="300" src="https://user-images.githubusercontent.com/106445479/192196670-e6118dbe-d524-44c9-9b3c-58dd435831db.gif">
</p>
<p align="center">Fig: Histogram vs Adaptive Histogram</p>


## References

- OpenCV documentation: https://docs.opencv.org/
- NumPy documentation: https://numpy.org/doc/stable/

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
