"""MAB Engine.
Author: Dohyung Park
Email: dohyung.prk@gmail.com
"""

import numpy as np
import scipy.stats as stats


class SimpleTS:
    """Simplified Thompson sampling class.
    ---
    Usage:
    >>> arms = [{'arm': 'a', trials: 10, wins: 0},
                {'arm': 'b', trials: 10, wins: 5}]
    >>> sts = SimpleTS(arms)
    >>> chosen_arm = sts.pull()
    """
    @staticmethod
    def _get_priors(arms: list) -> list:
        """Return Beta distrubtion list based on data source called arms.
        """
        priors = [
            stats.beta(a=1 + row['wins'], b=1 + row['trials'] - row['wins'])
            for row in arms
        ]
        return priors

    def __init__(self, arms: list) -> None:
        """Constructor
        """
        self.arms = arms
        self.priors = self._get_priors(arms)

    def pull(self) -> str:
        """Return chosen arm name
        """
        theta_samples = [d.rvs(1) for d in self.priors]
        chosen_bandit = np.argmax(theta_samples)
        return self.arms[chosen_bandit]['arm']

    def update_arm(self, arm: dict) -> None:
        """Update new arm to a object was made already.
        """
        self.arms.append(arm)
        self.priors += self._get_priors([arm])

    def update_priors(self, arms: list) -> None:
        """Update priors for online learning
        """
        self.arms = arms
        self.priors = self._get_priors(arms)
