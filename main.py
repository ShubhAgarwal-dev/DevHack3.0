from flask import Flask, render_template, request, redirect, url_for, jsonify
from pyweb.first import user_db
from blockchain.blockchain import Blockchain
from blockchain.image_block import ImageBlockChain
from pyweb.encrypt import EncryptImage


user_database = user_db(r'database\user.db')

app = Flask(__name__)

blockchain = Blockchain()
image_blockchain = ImageBlockChain(r'static\pictures', key=10)

user_name = 'ShubhAgarwal'


@app.route('/', methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        global user_name
        user_name = request.form.get("uname")
        # password = request.form.get("pword")
        if user_database.check_user_img2(user_name) > 0:
            return redirect(url_for('home'))
    return render_template('index.html')


@app.route('/home')
def home():
    name = str(request.args['uname']) or 'default'
    return render_template('homepage.html', name=name)


@app.route('/profile')
def profile():
    return render_template('profilepage.html', name=user_name)


@app.route('/jk')
def jk():
    name = str(request.args['uname']) or 'default'
    pas = str(request.args['pword']) or 'default'
    return f"It is now working {name} {pas}"


@app.route('/mine_block', methods=['GET'])
def mine_block():
    ''' Mining a New Block
    '''
    previous_block = blockchain.get_previous_block()
    proof = blockchain.proof_of_work(previous_block['proof'])
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)

    responce = {
        'message': 'Congratulations! You just mined the block',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': proof}

    return jsonify(responce), 200


@app.route('/get_chain', methods=['GET'])
def get_chain():
    ''' To get the chain
    '''
    responce = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(responce), 200


@app.route('/is_valid', methods=['GET'])
def is_valid():
    '''To check the validity of the chain created
    '''
    if blockchain.is_chain_valid(blockchain.chain):
        responce = {
            'message': 'All Good, BlockChain is Valid.'}
    else:
        responce = {
            'message': 'Opps!! BLockChain is not Valid'}
    return jsonify(responce), 200


if __name__ == '__main__':
    app.run(debug=True)
