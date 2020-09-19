//Mozilla Public License 2.0 
//As per https://github.com/ethereumjs/ethereumjs-vm/blob/master/LICENSE
//Requires the following packages to run as nodejs file https://gist.github.com/tpmccallum/0e58fc4ba9061a2e634b7a877e60143a

//Getting the requirements
var Trie = require('merkle-patricia-tree/secure');
var levelup = require('levelup');
var leveldown = require('leveldown');
var utils = require('ethereumjs-util');
var BN = utils.BN;
var Account = require('ethereumjs-account');

//Connecting to the leveldb database
var db = levelup(leveldown('/home/timothymccallum/gethDataDir/geth/chaindata'));

//Adding the "stateRoot" value from the block so that we can inspect the state root at that block height.
var root = '0x9369577baeb7c4e971ebe76f5d5daddba44c2aa42193248245cf686d20a73028';

//Creating a trie object of the merkle-patricia-tree library
var trie = new Trie(db, root);

var address = '0xccc6b46fa5606826ce8c18fece6f519064e6130b';
trie.get(address, function (err, raw) {
    if (err) return cb(err)
    //Using ethereumjs-account to create an instance of an account
    var account = new Account(raw)
    console.log('Account Address: ' + address);
    //Using ethereumjs-util to decode and present the account balance 
    console.log('Balance: ' + (new BN(account.balance)).toString());
})
