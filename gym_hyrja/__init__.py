import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Hyrja-v0',
    entry_point='gym_hyrja.envs:HyrjaEnv',
    nondeterministic = True,
)
