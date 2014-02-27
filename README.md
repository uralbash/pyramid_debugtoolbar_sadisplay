pyramid_debugtoolbar_sadisplay
======

pyramid_debugtoolbar_sadisplay will show project models as image,

Look how easy it is to use with Pyramid:

    # __init__.py
    # SADisplay in pyramid_debugtoolbar
    from pyramid_debugtoolbar_sadisplay.panel import SadisplayDebugPanel
    config.registry.settings['debugtoolbar.panels'].append(SadisplayDebugPanel)

and see...
1.*v
![ScreenShot](https://raw.github.com/uralbash/pyramid_debugtoolbar_sadisplay/master/docs/example.png)
2.*v
![ScreenShot](https://raw.github.com/uralbash/pyramid_debugtoolbar_sadisplay/master/docs/example2.png)

Installation
------------

Install from github:

    pip install git+http://github.com/uralbash/pyramid_debugtoolbar_sadisplay.git

Source:

    python setup.py install

Contribute
----------

- Issue Tracker: http://github.com/uralbash/pyramid_debugtoolbar_sadisplay/issues
- Source Code: http://github.com/uralbash/pyramid_debugtoolbar_sadisplay

Support
-------

If you are having issues, please let me know.
I have a mailing list located at: sacrud@uralbash.ru
