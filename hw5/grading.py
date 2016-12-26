"""
### NOTICE ###

You DO NOT need to upload this file.

"""
import sys, random
import tensorflow as tf

from agent import Agent
from environment import ALE

tf.set_random_seed(123)
random.seed(123)

init_seed = int(sys.argv[1])
init_rand = int(sys.argv[2])

config = tf.ConfigProto(allow_soft_placement = True)
config.gpu_options.allow_growth = True

with tf.Session(config=config) as sess:

    # Init env
    env = ALE(init_seed, init_rand)

    # Init agent
    agent = Agent(sess, env.ale.getMinimalActionSet())
    action_repeat, screen_type = agent.getSetting()

    # Set env setting
    env.setSetting(action_repeat, screen_type)

    # Get a new game
    screen = env.new_game()
    
    # Start playing
    current_reward = 0
    for _ in range(5000):
        action = agent.play(screen)
        reward, screen, terminal = env.act(action)
        current_reward += reward
        if terminal:
            break

    print("%d,%d,%d" % (init_seed, init_rand, current_reward))
