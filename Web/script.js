const display = document.getElementById('display');
const historyContent = document.getElementById('history-content');
let historyList = [];

function appendNumber(num) {
    if (display.value === '0' || display.value === 'Erro') {
        display.value = num;
    } else {
        display.value += num;
    }
}

function appendOperator(operator) {
    const lastChar = display.value.slice(-1);
    if ('+-*/'.includes(lastChar)) {
        display.value = display.value.slice(0, -1) + operator;
    } else {
        display.value += ' ' + operator + ' ';
    }
}

function clearDisplay() {
    display.value = '0';
}

function backspace() {
    if (display.value.length > 1) {
        display.value = display.value.slice(0, -1);
    } else {
        display.value = '0';
    }
}

function calculate() {
    try {
        const expression = display.value.replace(/×/g, '*').replace(/÷/g, '/');
        const result = eval(expression);
        
        // Adicionar ao histórico
        const operationText = `${display.value} = ${result}`;
        historyList.unshift(operationText);
        updateHistoryUI();

        display.value = result;
    } catch (error) {
        display.value = 'Erro';
    }
}

function updateHistoryUI() {
    if (historyList.length === 0) return;
    historyContent.innerHTML = historyList.map(item => `<div style="padding: 4px 0; border-bottom: 1px solid #2d3139; font-size:13px;">${item}</div>`).join('');
    historyContent.className = '';
}
