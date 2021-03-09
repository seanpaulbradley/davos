__all__ = ['smuggle']
version_info = (0, 0, 1)
__version__ = '.'.join(map(str, version_info))


from davos import config


def determine_environment():
    try:
        # noinspection PyUnresolvedReferences
        config.IPYTHON_SHELL = get_ipython()
    except NameError:
        return 'PY'
    else:
        import IPython
        if IPython.version_info[0] < 7:
            # running in Colaboratory or an old IPython/Jupyter
            # Notebook version
            return 'IPY_OLD'
        else:
            # running in a new(-ish) IPython/Jupyter Notebook version
            return 'IPY_NEW'


config.PARSER_ENVIRONMENT = determine_environment()

if config.PARSER_ENVIRONMENT == 'IPY_OLD':
    from davos.colab import smuggle_colab as smuggle
elif config.PARSER_ENVIRONMENT == 'IPY_NEW':
    from davos.jupyter import smuggle_jupyter as smuggle
else:
    from davos.python import smuggle_python as smuggle

smuggle._register_smuggler()