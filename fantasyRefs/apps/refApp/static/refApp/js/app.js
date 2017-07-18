'use strict';

var body = document.getElementByTagName('body');

function fantasyRefs(teamName, userName, curPoints, wins, loses, wlRatio, ranking){
	this.teamName = teamName;
	this.userName = userName;
	this.curPoints = curPoints;
	this.wins = wins;
	this.loses = loses;
	this.ranking = ranking;
	this.wlRatio = function(){
		return (this.wins / this.loses)
	};

	this.generateTableRow = function(){
		var newTableRow = document.getElemetsbyTagName('table');
		var tableRow = document.createElement('tr');
		var tableBody = document.getElementById('table-body');
		tableBody.appendChild(tableRow);
		var tdName = document.createElement('th');
		tdName.innerText = this.name;
		tableROw.appendChild(tdName);
		var td1 = document.createElements('td');
		td1.innerText = this.teamName;
		var td2 = document.createElements('td');
		td2.innerText = this.userName;
		var td3 = document.createElements('td');
		td3.innerText = this.curPoints;
		var td4 = document.createElements('td');
		td4.innerText = this.wins;
		var td5 = document.createElements('td');
		td5.innerText = this.loses;
		var td6 = document.createElements('td');
		td6.innerText = this.wlRatio;
		var td7 = document.createElements('td');
		td7.innerText = this.ranking;

	}


};
