# plot.py
# plot graph of one period of the sine and cosine functions

# modules
import numpy as np
import matplotlib.pyplot as plt

def main():
    # define x series
    x = np.linspace(start=0, stop=2 * np.pi)

    # plot
    plt.plot(x, np.sin(x), color="turquoise", label="sine")  # sine
    plt.plot(x, np.cos(x), color="moccasin", label="cosine")  # cosine
    plt.legend()
    plt.title("Sine and Cosine Plot")
    plt.xlabel("x")
    plt.ylabel("y", rotation=0)
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
