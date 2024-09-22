import os

from sftrain.python.common.constants import NodeEnv


def get_node_rank():
    """Get the node rank."""
    if NodeEnv.NODE_RANK in os.environ:
        rank = os.getenv(NodeEnv.NODE_RANK)
    else:
        # Backwards compatible env of elastic job with version < 0.3.0
        rank = os.getenv(NodeEnv.WORKER_RANK, "0")
    return int(rank)


def get_local_world_size():
    return int(os.getenv("LOCAL_WORLD_SIZE", 1))


def get_local_rank():
    return int(os.getenv("LOCAL_RANK", 0))


def get_rank():
    return int(os.getenv("RANK", 0))


def get_group_world_size():
    return int(os.getenv("GROUP_WORLD_SIZE", 1))


def get_group_rank():
    return int(os.getenv("GROUP_RANK", 1))


def get_torch_restart_count():
    return int(os.getenv("TORCHELASTIC_RESTART_COUNT", 0))


def get_node_id():
    """Get the node ID."""
    node_id = int(os.getenv(NodeEnv.NODE_ID, 0))
    return node_id


def get_node_type():
    """Get the node type."""
    node_type = os.getenv(NodeEnv.NODE_TYPE, "worker")
    return node_type


def get_node_num():
    """Get the number of node."""
    node_num = int(os.getenv(NodeEnv.NODE_NUM, 0))
    return node_num


def get_env(env_key):
    """Get the specified environment variable."""
    env_value = os.getenv(env_key, None)
    return env_value


def set_env(env_key, env_value):
    """Set the specified environment variable."""
    os.environ[env_key] = str(env_value)
