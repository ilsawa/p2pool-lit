from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    LightCoin=math.Object(
        PARENT=networks.nets['LightCoin'],
        SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=60, # shares
        SPREAD=30, # blocks
        IDENTIFIER='1d49d721309b8276'.decode('hex'),
        PREFIX='c790c5a9e60f1e11'.decode('hex'),
        P2P_PORT=4553,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=4554,
        BOOTSTRAP_ADDRS='crypto.office-on-the.net'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-lit',
        VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
