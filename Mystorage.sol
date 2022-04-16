// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Simple_storae {
    struct People {
        string name;
        uint256 _favnumber;
    }
    mapping(address => People) public people_map;

    constructor() {
        people_map[msg.sender] = People("Saksham", 7);
    }

    function SetFavnumber(uint256 num) public {
        people_map[msg.sender]._favnumber = num;
    }

    function SetName(string memory _name) public {
        people_map[msg.sender].name = _name;
    }
}
