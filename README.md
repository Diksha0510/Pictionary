# Pictionary
A real-time pictionary game against a bot.

**Load and Train Data**

Refer to the 'loadData_train.ipynb' for loading the data and training the neural network.

This model was trained on 40k images per pre-processed(full_......npy) file for the following classes:
1. Alarm clock
2. Bicycle
3. Bed
4. Airplane
5. Apple
6. Belt
7. Banana
8. Cake

The deep learning model has 2 convolutional layers and 1 GRU layer based on [1].

**Install and Play the game**

Execute the file 'pictionary.py' to start the game.

Requirements:

**References:**

1. Xu, P., Song, Z., Yin, Q., Song, Y., & Wang, L. (2020). Deep Self-Supervised Representation Learning for Free-Hand Sketch. IEEE Transactions on Circuits and Systems for Video Technology, 1-1. doi:10.1109/tcsvt.2020.3003048

2. [The Quick, Draw! Dataset](https://github.com/googlecreativelab/quickdraw-dataset)
