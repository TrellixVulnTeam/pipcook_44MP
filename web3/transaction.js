const Web3 = require('web3');
const Tx = require('ethereumjs-tx').Transaction; //交易事务
const rpcURL = 'https://ropsten.infura.io/v3/732bed0994c14471a2d4793e035bf944';
const web3 = new Web3(rpcURL);

const account1 = '0xD24C3559Aca63684493bf2a3eb6389F820d667Be';
const account2 = '0xc870A1d4Fa8feC179E3fC6b2195e7e92639d582b';

const privateKey1 = Buffer.from('b75e2bcaec74857cf9bb6636d66a04784d4c0fcfd908f4a2bc213428eba5af0d', 'hex');

let crypted = new Uint8Array(privateKey1.length );
for (let i = 0; i < privateKey1.length; ++i) {
    crypted[i ] = privateKey1[i];
}

console.log('pk', privateKey1);
console.log('ddd', crypted);
console.log('eee', crypted.length);
console.log('ppp', Buffer.concat([crypted]));


web3.eth.getTransactionCount(account1, (err, txCount) => {
    const txObject = {
        nonce: web3.utils.toHex(txCount), //前一个交易计数，必须是16进制
        to: account2, //目标账户
        value: web3.utils.toHex(web3.utils.toWei('0.1', 'ether')), //发送的以太币金额，十六进制
        gasLimit: web3.utils.toHex(21000), //交易消耗的gas的上限，最少花费21000wei
        gasPrice: web3.utils.toHex(web3.utils.toWei('10', 'gwei')) // Gas的价格，
    }

    /**签署交易 */
    const tx = new Tx(txObject, { chain: 'ropsten', hardfork: 'petersburg' }); //ropsten 网络
    tx.sign(privateKey1); //privateKey1
    const serializedTx = tx.serialize();
    const raw = '0x' + serializedTx.toString('hex');

    /**广播交易 */
    web3.eth.sendSignedTransaction(raw, (err, txHash) => {
        console.log('===>>err', err);
        console.log('txHash: %s', txHash);
    })
})


