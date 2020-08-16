inf = float('inf')

commands_config = {
    'admin': {
        '/ddos': {
            'param': {
                't': {
                    'name': 'time',
                    'argnum': 1,
                    'argtype': int,
                    'lim': inf
                },
                'n': {
                    'name': 'number',
                    'argnum': 1,
                    'argtype': str
                },
                'stop': {
                    'name': 'stop',
                    'argnum': 0,
                    'default': True,
                    'next_param': 'n'
                },
                'info': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'info'
                },
                'h': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'help'
                }
            },
            'lim': {
                'simult': inf,
                'daylim': inf
            }
        },
        '/bl': {
            'param': {
                'n': {
                    'name': 'number',
                    'argnum': 1,
                    'argtype': str
                },
                'add': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'add',
                    'next_param': 'n'
                },
                'del': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'del',
                    'next_param': 'n'
                },
                'info': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'info'
                },
                'h': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'help'
                }
            },
            'lim': {
                'datalim': inf
            }
        },
        '/set': {
            'param': {
                'id': {
                    'name': 'target_id',
                    'argnum': 1,
                    'argtype': int
                },
                'stat': {
                    'name': 'status',
                    'argnum': 1,
                    'argtype': str
                },
                'info': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'info'
                },
                'h': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'help'
                }
            },
            'lim': {}
        },
        '/help': {}
    },
    'vip_3': {
        '/ddos': {
            'param': {
                't': {
                    'name': 'time',
                    'argnum': 1,
                    'argtype': int,
                    'lim': 3000
                },
                'n': {
                    'name': 'number',
                    'argnum': 1,
                    'argtype': str
                },
                'stop': {
                    'name': 'stop',
                    'argnum': 0,
                    'default': True,
                    'next_param': 'n'
                },
                'info': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'info'
                },
                'h': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'help'
                }
            },
            'lim': {
                'simult': 4,
                'daylim': inf
            }
        },
        '/bl': {
            'param': {
                'n': {
                    'name': 'number',
                    'argnum': 1,
                    'argtype': str
                },
                'add': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'add',
                    'next_param': 'n'
                },
                'del': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'del',
                    'next_param': 'n'
                },
                'info': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'info'
                },
                'h': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'help'
                }
            },
            'lim': {
                'datalim': 4
            }
        },
        '/help': {}
    },
    'vip_2': {
        '/ddos': {
            'param': {
                't': {
                    'name': 'time',
                    'argnum': 1,
                    'argtype': int,
                    'lim': 2000
                },
                'n': {
                    'name': 'number',
                    'argnum': 1,
                    'argtype': str
                },
                'stop': {
                    'name': 'stop',
                    'argnum': 0,
                    'default': True,
                    'next_param': 'n'
                },
                'info': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'info'
                },
                'h': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'help'
                }
            },
            'lim': {
                'daylim': 40,
                'simult': 3
            }
        },
        '/bl': {
            'param': {
                'n': {
                    'name': 'number',
                    'argnum': 1,
                    'argtype': str
                },
                'add': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'add',
                    'next_param': 'n'
                },
                'del': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'del',
                    'next_param': 'n'
                },
                'info': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'info'
                },
                'h': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'help'
                }
            },
            'lim': {
                'datalim': 3
            }
        },
        '/help': {}
    },
    'vip_1': {
        '/ddos': {
            'param': {
                't': {
                    'name': 'time',
                    'argnum': 1,
                    'argtype': int,
                    'lim': 1000
                },
                'n': {
                    'name': 'number',
                    'argnum': 1,
                    'argtype': str
                },
                'stop': {
                    'name': 'stop',
                    'argnum': 0,
                    'default': True,
                    'next_param': 'n'
                },
                'info': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'info'
                },
                'h': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'help'
                }
            },
            'lim': {
                'daylim': 40,
                'simult': 2
            }
        },
        '/bl': {
            'param': {
                'n': {
                    'name': 'number',
                    'argnum': 1,
                    'argtype': str
                },
                'add': {
                    'name': 'command',
                    'argnum': 1,
                    'default': 'add',
                    'next_param': 'n'
                },
                'del': {
                    'name': 'command',
                    'argnum': 1,
                    'default': 'del',
                    'next_param': 'n'
                },
                'info': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'info'
                },
                'h': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'help'
                }
            },
            'lim': {
                'datalim': 1
            }
        },
        '/help': {}
    },
    'user': {
        '/ddos': {
            'param': {
                't': {
                    'name': 'time',
                    'argnum': 1,
                    'argtype': int,
                    'lim': 99
                },
                'n': {
                    'name': 'number',
                    'argnum': 1,
                    'argtype': str
                },
                'stop': {
                    'name': 'stop',
                    'argnum': 0,
                    'default': True,
                    'next_param': 'n'
                },
                'info': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'info'
                },
                'h': {
                    'name': 'command',
                    'argnum': 0,
                    'default': 'help'
                }
            },
            'lim': {
                'daylim': 10,
                'simult': 1
            }
        },
        '/help': {}
    }
}
