from enum import Enum

available_commands = {
    'admin': {
        'ddos': {
            'time': float("inf"),
            'th': float("inf"),
            'count': float("inf")
        },
        'bl': {
            'add': float("inf"),
            'rem': float("inf"),
            'ls': 1
        }
    },
    'user': {
        'ddos': {
            'time': 99,
            'th': 15,
            'count': 1
        },
        'bl': {
            'add': 0,
            'rem': 0,
            'ls': 1
        }
    },
    'vip_1': {
        'ddos': {
            'time': 1000,
            'th': 15,
            'count': 2
        },
        'bl': {
            'add': 2,
            'rem': float("inf"),
            'ls': 1
        }
    },
    'vip_2': {
        'ddos': {
            'time': 2000,
            'th': 15,
            'count': 3
        },
        'bl': {
            'add': 3,
            'rem': float("inf"),
            'ls': 1
        }
    },
    'vip_3': {
        'ddos': {
            'time': 3000,
            'th': 15,
            'count': 4
        },
        'bl': {
            'add': 4,
            'rem': float("inf"),
            'ls': 1
        }
    }
}

commands_config = {
    'admin' : {
        '/ddos' :
        ({
            't': {
                'name' : 'time',
                'anum' : 1,
                'atype': int,
                'lim'  : float('inf')
            },
            'n': {
                'name' : 'number',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            },
            'stop': {
                'name' : 'stop',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            }
        }, float('inf')),
        '/bl':
        ({
            'add': {
                'name' : 'command',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            },
            'del': {
                'name' : 'command',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            }
        }, float('inf')),
        '/info':
        ({
            'h': {
                'name' : 'command',
                'anum' : 0
            },
            'bl': {
                'name' : 'command',
                'anum' : 0
            },
            'ddos': {
                'name' : 'command',
                'anum' : 0
            },
        }, float('inf'))
    },
    'vip_1': {
        '/ddos':
        ({
            't': {
                'name' : 'time',
                'anum' : 1,
                'atype': int,
                'lim'  : 3600
            },
            'n': {
                'name' : 'number',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            },
            'stop': {
                'name' : 'stop',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            }
        }, 50),
        '/bl':
        ({
            'add': {
                'name' : 'command',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            },
            'del': {
                'name' : 'command',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            }
        }, float('inf')),
        '/info':
        ({
            'h': {
                'name' : 'command',
                'anum' : 0
            },
            'bl': {
                'name' : 'command',
                'anum' : 0
            },
            'ddos': {
                'name' : 'command',
                'anum' : 0
            }
        }, float('inf'))
    },
    'vip_2': {
        '/ddos':
        ({
            't': {
                'name' : 'time',
                'anum' : 1,
                'atype': int,
                'lim'  : 3600
            },
            'n': {
                'name' : 'number',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            },
            'stop': {
                'name' : 'stop',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            }
        }, 100),
        '/bl':
        ({
            'add': {
                'name' : 'command',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            },
            'del': {
                'name' : 'command',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            }
        }, float('inf')),
        '/info':
        ({
            'h': {
                'name' : 'command',
                'anum' : 0
            },
            'bl': {
                'name' : 'command',
                'anum' : 0
            },
            'ddos': {
                'name' : 'command',
                'anum' : 0
            }
        }, float('inf'))
    },
    'vip_3': {
        '/ddos':
        ({
            't': {
                'name' : 'time',
                'anum' : 1,
                'atype': int,
                'lim'  : 3600
            },
            'n': {
                'name' : 'number',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            },
            'stop': {
                'name' : 'number',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            }
        }, 200),
        '/bl':
        ({
            'add': {
                'name' : 'command',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            },
            'del': {
                'name' : 'command',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            }
        }, float('inf')),
        '/info':
        ({
            'h': {
                'name' : 'command',
                'anum' : 0
            },
            'bl': {
                'name' : 'command',
                'anum' : 0
            },
            'ddos': {
                'name' : 'command',
                'anum' : 0
            }
        }, float('inf'))
    },
    'user': {
        '/ddos':
        ({
            't': {
                'name' : 'time',
                'anum' : 1,
                'atype': int,
                'lim'  : 150
            },
            'n': {
                'name' : 'number',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            },
            'stop': {
                'name' : 'stop',
                'anum' : 1,
                'atype': str,
                'lim'  : -1
            }
        }, 15),
        '/info':
        ({
            'h': {
                'name' : 'command',
                'anum' : 0
            },
            'ddos': {
                'name' : 'command',
                'anum' : 0
            },
        }, float('inf'))
    }
}