// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EquiterraInvest {
    struct Startup {
        string name;
        string idea;
        uint fundingRequired;
        address founder;
    }

    Startup[] public startups;

    event StartupSubmitted(string name, address founder);

    function submitStartup(string memory _name, string memory _idea, uint _fundingRequired) public {
        startups.push(Startup(_name, _idea, _fundingRequired, msg.sender));
        emit StartupSubmitted(_name, msg.sender);
    }

    function getStartup(uint index) public view returns (string memory, string memory, uint, address) {
        Startup memory s = startups[index];
        return (s.name, s.idea, s.fundingRequired, s.founder);
    }

    function getStartupCount() public view returns (uint) {
        return startups.length;
    }
}
