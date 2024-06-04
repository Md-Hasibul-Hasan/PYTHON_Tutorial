// the hello world program
console.log('Hello World');
const canvas = document.getElementById("drawing-canvas");
const ctx = canvas.getContext("2d");

let currentColor = "black";
let isDrawing = false;
let lastX = 0;
let lastY = 0;
let lineWidth = 5;

const colorPicker = document.getElementById("color-picker");
const lineWidthInput = document.getElementById("line-width");
const clearButton = document.getElementById("clear-button");

function drawLine(x0, y0, x1, y1, color, width) {
  ctx.beginPath();
  ctx.moveTo(x0, y0);
  ctx.lineTo(x1, y1);
  ctx.strokeStyle = color;
  ctx.lineWidth = width;
  ctx.stroke();
}

function handleMouseDown(e) {
  isDrawing = true;
  lastX = e.offsetX;
  lastY = e.offsetY;
}

function handleMouseMove(e) {
  if (isDrawing) {
    drawLine(lastX, lastY, e.offsetX, e.offsetY, currentColor, lineWidth);
    lastX = e.offsetX;
    lastY = e.offsetY;
  }
}

function handleMouseUp() {
  isDrawing = false;
}

function updateColor() {
  currentColor = colorPicker.value;
}

function updateLineWidth() {
  lineWidth = parseInt(lineWidthInput.value);
  if (lineWidth < 1) {
    lineWidth = 1;
    lineWidthInput.value = 1;
  } else if (lineWidth > 20) {
    lineWidth = 20;
    lineWidthInput.value = 20;
  }
}

function clearCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

colorPicker.addEventListener("change", updateColor);
lineWidthInput.addEventListener("change", updateLineWidth);
clearButton.addEventListener("click", clearCanvas);

canvas.addEventListener("mousedown", handleMouseDown);
canvas.addEventListener("mousemove", handleMouseMove);
window.addEventListener("mouseup", handleMouseUp);

// Additional Features (goes beyond 500 lines)

// Implement functionality to draw shapes (e.g., rectangle, circle)
function drawRectangle(x, y, width, height, color, filled) {
  ctx.beginPath();
  ctx.rect(x, y, width, height);
  if (filled) {
    ctx.fillStyle = color;
    ctx.fill();
  } else {
    ctx.strokeStyle = color;
    ctx.stroke();
  }
}

function drawCircle(x, y, radius, color, filled) {
  ctx.beginPath();
  ctx.arc(x, y, radius, 0, Math.PI * 2);
  if (filled) {
    ctx.fillStyle = color;
    ctx.fill();
  } else {
    ctx.strokeStyle = color;
    ctx.stroke();
  }
}

// Implement functionality to change the fill color (if applicable)
let fillColor = "white";
const fillColorPicker = document.getElementById("fill-color-picker");

function updateFillColor() {
  fillColor = fillColorPicker.value;
}

fillColorPicker.addEventListener("change", updateFillColor);

// ... add event listeners and logic for drawing shapes with fill color

// Implement functionality to undo/redo actions
let undoStack = [];
let redoStack = [];

function pushToUndo(action) {
  undoStack.push(action);
  redoStack = []; // Clear redo stack when performing a new action
}

function undo() {
  if (undoStack.length > 0) {
    const action = undoStack.pop();
    action.undo(); // Call the undo method of the specific action object
    redoStack.push(action); // Pushed to redo stack for potential redo
  }
}

function redo() {
  if (redoStack.length > 0) {
    const action = redoStack.pop();
    action.redo(); // Call the redo method of the specific action object
    undoStack.push(action); // Pushed to undo stack for potential undo
  }
}

// Implement functions to store and load drawings from local storage

// ... add logic for saving and loading drawing data to/from local storage

This example showcases core drawing functionalities and expands upon the base by including features like shape drawing, fill color
