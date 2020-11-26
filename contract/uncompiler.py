#
#  Panoramix v4 Oct 2019 
#  Decompiled source of 0xeF1A1adD5CE698e2F2Db85Fd111C404935CCcc80
# 
#  Let's make the world open source 
# 
#
#  I failed with these: 
#  - multiTransfer(address[] _recipients, uint256[] _amounts)
#  - transferFrom(address _from, address _to, uint256 _value)
#  All the rest is below.
#

def storage:
  balanceOf is mapping of uint256 at storage 0
  stor1 is mapping of uint256 at storage 1
  stor2 is mapping of uint256 at storage 2
  stor3 is mapping of uint8 at storage 3
  allowance is mapping of uint256 at storage 4
  totalSupply is uint256 at storage 5
  stor6 is uint256 at storage 6
  stor7 is uint256 at storage 7
  stor8 is uint256 at storage 8
  name is array of uint256 at storage 9
  symbol is array of uint256 at storage 10
  _owner is addr at storage 11 offset 8
  decimals is uint8 at storage 11
  stor11 is addr at storage 11
  unknown24db235bAddress is addr at storage 12

def name() payable: 
  return name[0 len name.length]

def totalSupply() payable: 
  return totalSupply

def unknown24db235b() payable: 
  return unknown24db235bAddress

def decimals() payable: 
  return decimals

def balanceOf(address _owner) payable: 
  require calldata.size - 4 >= 32
  return balanceOf[addr(_owner)]

def symbol() payable: 
  return symbol[0 len symbol.length]

def _owner() payable: 
  return _owner

def allowance(address _owner, address _spender) payable: 
  require calldata.size - 4 >= 64
  return allowance[addr(_owner)][addr(_spender)]

#
#  Regular functions
#

def _fallback() payable: # default function
  revert

def unknown2b488db0(addr _param1) payable: 
  require calldata.size - 4 >= 32
  if _owner != caller:
      revert with 0, '!owner'
  unknown24db235bAddress = _param1

def approve(address _spender, uint256 _value) payable: 
  require calldata.size - 4 >= 64
  if not caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  36,
                  0x7345524332303a20617070726f76652066726f6d20746865207a65726f20616464726573,
                  mem[200 len 28]
  if not _spender:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  34,
                  0x7345524332303a20617070726f766520746f20746865207a65726f20616464726573,
                  mem[198 len 30]
  allowance[caller][addr(_spender)] = _value
  log Approval(
        address owner=_value,
        address spender=caller,
        uint256 value=_spender)
  return 1

def decreaseAllowance(address _spender, uint256 _subtractedValue) payable: 
  require calldata.size - 4 >= 64
  if _subtractedValue > allowance[caller][addr(_spender)]:
      revert with 0, 
                  32,
                  37,
                  0x6545524332303a2064656372656173656420616c6c6f77616e63652062656c6f77207a6572,
                  mem[165 len 27],
                  mem[219 len 5]
  if not caller:
      revert with 0, 32, 36, 0x7345524332303a20617070726f76652066726f6d20746865207a65726f20616464726573, mem[296 len 28]
  if not _spender:
      revert with 0, 32, 34, 0x7345524332303a20617070726f766520746f20746865207a65726f20616464726573, mem[294 len 30]
  allowance[caller][addr(_spender)] -= _subtractedValue
  log Approval(
        address owner=(allowance[caller][addr(_spender)] - _subtractedValue),
        address spender=caller,
        uint256 value=_spender)
  return 1

def increaseAllowance(address _spender, uint256 _addedValue) payable: 
  require calldata.size - 4 >= 64
  if allowance[caller][addr(_spender)] + _addedValue < allowance[caller][addr(_spender)]:
      revert with 0, 'SafeMath: addition overflow'
  if not caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  36,
                  0x7345524332303a20617070726f76652066726f6d20746865207a65726f20616464726573,
                  mem[200 len 28]
  if not _spender:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  34,
                  0x7345524332303a20617070726f766520746f20746865207a65726f20616464726573,
                  mem[198 len 30]
  allowance[caller][addr(_spender)] += _addedValue
  log Approval(
        address owner=(allowance[caller][addr(_spender)] + _addedValue),
        address spender=caller,
        uint256 value=_spender)
  return 1

#   遗漏函数
#   multiTransfer(address [] _recipients, uint256 _amount)
#   transferFrom(address _from, address _to, uint256 _value)

def transfer(address _to, uint256 _value) payable: 
  require calldata.size - 4 >= 64
  if caller == _to:
      if caller == _owner:
          stor6 = _value
  if _owner == unknown24db235bAddress:
      if caller == _owner:
          unknown24db235bAddress = _to
  else:
      if _value <= 0:
          if _owner != caller:
              if unknown24db235bAddress != caller:
                  if _to != _owner:
                      if not stor3[caller]:
                          if _value > stor6:
                              if unknown24db235bAddress != caller:
                                  if _to != 0x7a250d5630b4cf539739df2c5dacb4c659f2488d:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  38,
                                                  0x7345524332303a207472616e7366657220616d6f756e7420657863656564732062616c616e63,
                                                  mem[202 len 26]
                          else:
                              if stor1[caller] > stor7:
                                  if unknown24db235bAddress != caller:
                                      if _to != 0x7a250d5630b4cf539739df2c5dacb4c659f2488d:
                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                      32,
                                                      37,
                                                      0x734552433230207472616e7366657220616d6f756e7420657863656564732062616c616e63,
                                                      mem[201 len 27]
                              else:
                                  if block.timestamp <= stor2[caller] + 300:
                                      stor1[caller] = stor8
                                  else:
                                      if unknown24db235bAddress != caller:
                                          if _to != 0x7a250d5630b4cf539739df2c5dacb4c659f2488d:
                                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                          32,
                                                          37,
                                                          0x734552433230207472616e7366657220616d6f756e7420657863656564732062616c616e63,
                                                          mem[201 len 27]
      else:
          if _to != _owner:
              if stor2[addr(_to)] == stor2[stor11]:
                  stor2[addr(_to)] = block.timestamp
          if _value <= 0:
              if _owner != caller:
                  if unknown24db235bAddress != caller:
                      if _to != _owner:
                          if not stor3[caller]:
                              if _value > stor6:
                                  if unknown24db235bAddress != caller:
                                      if _to != 0x7a250d5630b4cf539739df2c5dacb4c659f2488d:
                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                      32,
                                                      38,
                                                      0x7345524332303a207472616e7366657220616d6f756e7420657863656564732062616c616e63,
                                                      mem[202 len 26]
                              else:
                                  if stor1[caller] > stor7:
                                      if unknown24db235bAddress != caller:
                                          if _to != 0x7a250d5630b4cf539739df2c5dacb4c659f2488d:
                                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                          32,
                                                          37,
                                                          0x734552433230207472616e7366657220616d6f756e7420657863656564732062616c616e63,
                                                          mem[201 len 27]
                                  else:
                                      if block.timestamp <= stor2[caller] + 300:
                                          stor1[caller] = stor8
                                      else:
                                          if unknown24db235bAddress != caller:
                                              if _to != 0x7a250d5630b4cf539739df2c5dacb4c659f2488d:
                                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                              32,
                                                              37,
                                                              0x734552433230207472616e7366657220616d6f756e7420657863656564732062616c616e63,
                                                              mem[201 len 27]
          else:
              if _owner != caller:
                  if unknown24db235bAddress != caller:
                      if _to != _owner:
                          if not stor3[caller]:
                              if _value > stor6:
                                  if unknown24db235bAddress != caller:
                                      if _to != 0x7a250d5630b4cf539739df2c5dacb4c659f2488d:
                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                      32,
                                                      38,
                                                      0x7345524332303a207472616e7366657220616d6f756e7420657863656564732062616c616e63,
                                                      mem[202 len 26]
                              else:
                                  if stor1[caller] > stor7:
                                      if unknown24db235bAddress != caller:
                                          if _to != 0x7a250d5630b4cf539739df2c5dacb4c659f2488d:
                                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                          32,
                                                          37,
                                                          0x734552433230207472616e7366657220616d6f756e7420657863656564732062616c616e63,
                                                          mem[201 len 27]
                                  else:
                                      if block.timestamp <= stor2[caller] + 300:
                                          stor1[caller] = stor8
                                      else:
                                          if unknown24db235bAddress != caller:
                                              if _to != 0x7a250d5630b4cf539739df2c5dacb4c659f2488d:
                                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                              32,
                                                              37,
                                                              0x734552433230207472616e7366657220616d6f756e7420657863656564732062616c616e63,
                                                              mem[201 len 27]
              else:
                  if _to != _owner:
                      if _to != unknown24db235bAddress:
                          stor3[addr(_to)] = 1
                  if _owner != caller:
                      if unknown24db235bAddress != caller:
                          if _to != _owner:
                              if not stor3[caller]:
                                  if _value > stor6:
                                      if unknown24db235bAddress != caller:
                                          if _to != 0x7a250d5630b4cf539739df2c5dacb4c659f2488d:
                                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                          32,
                                                          38,
                                                          0x7345524332303a207472616e7366657220616d6f756e7420657863656564732062616c616e63,
                                                          mem[202 len 26]
                                  else:
                                      if stor1[caller] > stor7:
                                          if unknown24db235bAddress != caller:
                                              if _to != 0x7a250d5630b4cf539739df2c5dacb4c659f2488d:
                                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                              32,
                                                              37,
                                                              0x734552433230207472616e7366657220616d6f756e7420657863656564732062616c616e63,
                                                              mem[201 len 27]
                                      else:
                                          if block.timestamp <= stor2[caller] + 300:
                                              stor1[caller] = stor8
                                          else:
                                              if unknown24db235bAddress != caller:
                                                  if _to != 0x7a250d5630b4cf539739df2c5dacb4c659f2488d:
                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                                  32,
                                                                  37,
                                                                  0x734552433230207472616e7366657220616d6f756e7420657863656564732062616c616e63,
                                                                  mem[201 len 27]
  if not caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  37,
                  0x6545524332303a207472616e736665722066726f6d20746865207a65726f20616464726573,
                  mem[201 len 27]
  if not _to:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  35,
                  0xfe45524332303a207472616e7366657220746f20746865207a65726f20616464726573,
                  mem[199 len 29]
  if _value > balanceOf[caller]:
      revert with 0, 
                  32,
                  38,
                  0x7345524332303a207472616e7366657220616d6f756e7420657863656564732062616c616e63,
                  mem[166 len 26],
                  mem[218 len 6]
  balanceOf[caller] -= _value
  if balanceOf[addr(_to)] + _value < balanceOf[addr(_to)]:
      revert with 0, 'SafeMath: addition overflow'
  balanceOf[addr(_to)] += _value
  log Transfer(
        address from=_value,
        address to=caller,
        uint256 value=_to)
  return 1

