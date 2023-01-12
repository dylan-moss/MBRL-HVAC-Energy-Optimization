import numpy as np
from beobench.experiment.provider import config

from hnp.agents import QLearningAgent
from hnp.environment import ObservationWrapper, create_env


def main():
    # Create environment and wrap observations

    obs_to_keep = np.array([0, 1, 8]) 
    lows = np.array([0, 0, 0])
    highs = np.array([1, 1, 1])
    mask = np.array([0, 0, 0])

    env = create_env(config["env"]["config"])
    env = ObservationWrapper(env, obs_to_keep)

    agent = QLearningAgent(
        env, 
        config["agent"]["config"],
        mask,
        lows,
        highs,
        results_dir=config["general"]["local_dir"],
        use_beobench=True
    )
    agent.train()
    agent.save_results()
    env.close()

if __name__ == "__main__":
    main()