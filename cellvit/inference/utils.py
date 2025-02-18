import os
import multiprocessing


def get_slurm_cpus():
    """Detect available CPUs in a Slurm job or fallback to system CPU count."""
    if "SLURM_CPUS_PER_TASK" in os.environ:
        return int(os.environ["SLURM_CPUS_PER_TASK"])
    elif "SLURM_JOB_CPUS_PER_NODE" in os.environ:
        return sum(map(int, os.environ["SLURM_JOB_CPUS_PER_NODE"].split(",")))
    elif "SLURM_NTASKS" in os.environ and "SLURM_NTASKS_PER_NODE" in os.environ:
        return int(os.environ["SLURM_NTASKS_PER_NODE"]) * int(os.environ["SLURM_NTASKS"])
    else:
        return multiprocessing.cpu_count()
