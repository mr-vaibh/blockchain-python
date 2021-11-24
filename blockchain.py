from datetime import datetime
from hashlib import sha256
import json

class Block:
    def __init__(self, previousHash, data):
        self.data = data
        self.previousHash = previousHash
        self.timeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.proofOfWork = 0
        self.hash = self.calculateHash()
    
    def calculateHash(self):
        return sha256(
            (
                self.previousHash +
                json.dumps(self.data) +
                self.timeStamp +
                str(self.proofOfWork)
            )
            .encode() # encoding before hashing
        ).hexdigest()
    
    def mine(self, difficulty):
        # find the hash
        while not self.hash.startswith('0' * difficulty):
            self.proofOfWork += 1
            self.hash = self.calculateHash()


class Blockchain:
    def __init__(self):
        genesisBlock = Block('0', {'isGenesis': True})
        self.chain = [genesisBlock]
    
    def addBlock(self, data):
        lastBlock = self.chain[len(self.chain) - 1]
        newBlock = Block(lastBlock.hash, data)
        newBlock.mine(2) # find a hash for new block
        self.chain.append(newBlock)
    
    def getLatestBlock(self):
        return self.chain[-1]
    
    def isValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i - 1]

            if currentBlock.hash != currentBlock.calculateHash(): return False
            if currentBlock.previousHash != previousBlock.hash: return False
        return True


blockchain = Blockchain()

blockchain.addBlock({
    'from': 'Vaibhav',
    'to': 'Anubhav',
    'amount': 100
})

blockchain.addBlock({
    'from': 'Anubhav',
    'to': 'David',
    'amount': 150
})
