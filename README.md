# gabaithon202309_team2_back

## Start Up with Docker
```bash
docker compose up python
docker compose exec python bash
# 色々実行
```
## Start Up
Windowsの人はWSL上で行うことをお勧めします
```bash
pip3 install pipenv
pipenv install

pipenv run dev
# http://localhost:8000　にアクセス
```

## API Doc
https://scla-sagauniv.github.io/gabaithon202309_team2_back/dist/

## mockup
```
yarn global add @stoplight/prism-cli
prism mock docs/swagger.yaml
```