npm init -y
npm install --save-dev rollup
echo "building venv..."
python3 -m venv myvenv
echo "done"
. ./myvenv/bin/activate
pip3 install  addict transcrypt

python3 setup.py

npm run rollup
