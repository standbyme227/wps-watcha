FROM        standbyme227/project:base

ENV         BUILD_MODE             production
ENV         DJANGO_SETTINGS_MODULE config.settings.production

COPY        . /srv/project

RUN         cp -f /srv/project/.config/${BUILD_MODE}/nginx.conf     /etc/nginx/nginx.conf &&\
            cp -f /srv/project/.config/${BUILD_MODE}/nginx-app.conf /etc/nginx/sites-available/ &&\
            rm -f /etc/nginx/sites-enabled/* &&\
            ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/

RUN         cp /srv/project/.config/${BUILD_MODE}/supervisord.conf /etc/supervisor/conf.d/


CMD         pkill nginx; supervisord -n

EXPOSE      80



