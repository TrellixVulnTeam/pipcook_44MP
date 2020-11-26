const Web3 = require('web3');
const Tx = require('ethereumjs-tx').Transaction; //交易事务
const rpcURL = 'https://kovan.infura.io/v3/732bed0994c14471a2d4793e035bf944';
const web3 = new Web3(rpcURL);

const address = '0x03118E2c88676d31ee397E1eEf7789fECfbC40b9';

/**查询余额  */
web3.eth.getBalance(address, (err, wei) => {
    let balance = web3.utils.fromWei(wei, 'ether'); //余额单位从wei 转为 ether
    console.log('address: %s 的余额是: %d', address, balance);
})

/**测试合约 */