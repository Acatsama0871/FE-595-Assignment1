# plot.py
# plot graph of one period of the sine and cosine functions

# modules
import numpy as np
import matplotlib.pyplot as plt


def main():

    # define x series
    x = np.linspace(start=0, stop=2 * np.pi)

    tan_x = np.linspace(start=0, stop=2 * np.pi)  # added by Baihao Huang
    tan_y = np.tan(x)  # added by Baihao Huang
    max_index = tan_y.argmax()  # added by Baihao Huang
    min_idex = tan_y.argmin()  # added by Baihao Huang

    tan_x[max_index] = np.nan  # added by Baihao Huang
    tan_x[min_idex] = np.nan  # added by Baihao Huang
    tan_y[max_index] = np.nan  # added by Baihao Huang
    tan_y[min_idex] = np.nan  # added by Baihao Huang

    # plot
    plt.plot(x, np.sin(x), color="turquoise", label="sine")  # sine
    plt.plot(x, np.cos(x), color="moccasin", label="cosine")  # cosine
    plt.plot(tan_x, tan_y, color="red", label="tan")  # added by Baihao Huang
    plt.ylim(-1, 1)  # added by Baihao Huang
    plt.legend()
    plt.title("Sine and Cosine Plot")
    plt.xlabel("x")
    plt.ylabel("y", rotation=0)
    plt.grid()
    plt.show()


if __name__ == "__main__" :
    main()
