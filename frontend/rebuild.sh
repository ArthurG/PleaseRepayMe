npm run build
mkdir ../backend/app/static/
mkdir ../backend/app/static/css
mkdir ../backend/app/static/js
mkdir ../backend/app/static/img
mkdir ../backend/app/templates
cp dist/static/css/* ../backend/app/static/css/
cp dist/static/js/* ../backend/app/static/js/
cp dist/static/img/* ../backend/app/static/img/
cp dist/index.html ../backend/app/templates/

