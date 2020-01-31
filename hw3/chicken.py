import numpy as np
import matplotlib.pyplot as plt

def new_distribution(hp_loc=1.5, hp_scale=0.25):
    dist_mu = np.random.normal(loc=hp_loc, scale=hp_scale)
    dist_var = np.random.normal(loc=hp_loc, scale=hp_scale)
    dist_mu = max(0, dist_mu)
    dist_var = max(0, dist_var)
    return (dist_mu, dist_var)

menu = '''
Enter n to get a new distribution for reaction times.
Enter d to get the reaction time distribution parameters.
To view the history of reaction times and sample means, enter h.
Otherwise, enter your reaction time as a floating point value.
Please pick a positive floating point value between 0 and 1.
Any invalid value will default to 0.
'''

if __name__ == "__main__":
    print(menu)
    rt_loc, rt_scale = new_distribution()
    recorded_rt, sample_means = [], []
    while(True):
        pl1 = raw_input("Player 1's move: ")
        pl2 = raw_input("Player 2's move: ")
        if pl1 == "n" or pl2 == "n":
            rt_loc, rt_scale = new_distribution()
            recorded_rt, sample_means = [], []
        elif pl1 == "d" or pl2 == "d":
            print("mu: {}, var: {}".format(rt_loc, rt_scale))
        elif pl1 == "h" or pl2 == "h":
            print("Reaction times:")
            print(recorded_rt)
            print("Sample means:")
            print(sample_means)
            plt.figure()
            plt.title("Reaction times and sample means")
            plt.plot(range(len(recorded_rt)),recorded_rt,label="Reaction times")
            plt.plot(range(len(sample_means)),sample_means,label="Sample means")
            plt.legend()
            plt.show()
            plt.figure()
            plt.title("Reaction times and sample means")
            plt.hist(recorded_rt,label="Reaction times",alpha=0.5)
            plt.hist(sample_means,label="Sample means",alpha=0.5)
            plt.legend()
            plt.show()
        else:
            try:
                pl1 = float(pl1)
                pl1 = max(pl1, 0)
                pl1 = min(pl1, 10)
            except:
                print("Issue parsing player 1's input, defaulting move to 0.")
                pl1 = 0
            try:
                pl2 = float(pl2)
                pl2 = max(pl2, 0)
                pl2 = min(pl2, 10)
            except:
                print("Issue parsing player 2's input, defaulting move to 0.")
                pl2 = 0
            rt = np.random.normal(loc=rt_loc, scale=rt_scale)
            rt = max(0,rt)
            rt = min(10,rt)
            recorded_rt.append(rt)
            sample_means.append(np.mean(recorded_rt))
            print("Reaction time: {}".format(rt))
            print("Player 1's move: {}".format(pl1))
            print("Player 2's move: {}".format(pl2))
            if (pl1 <= rt and pl2 <= rt):
                print("YOU BOTH CRASH!!!")
            elif pl1 == pl2:
                print("You both swerve at the same time and tie!")
            elif pl1 < pl2:
                print("Player 1 swerves first -- Player 2 wins!")
            else:
                print("Player 2 swerves first -- Player 1 wins!")