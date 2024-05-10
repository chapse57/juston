const plusButton = document.getElementById('plusButton');
const resetButton = document.getElementById('resetButton');
const clickCount = document.getElementById('clickCount');
const minusButton = document.getElementById('minusButton');

// 카운트를 저장할 변수를 초기화합니다.
let count = 0;

// 버튼 클릭 이벤트에 대한 핸들러를 추가합니다.
plusButton.addEventListener('click', function() {
  // 클릭할 때마다 카운트를 증가시킵니다.
  count++;

  // 증가된 카운트를 표시합니다.
  clickCount.textContent = count;
});

minusButton.addEventListener('click', function() {
  // 클릭할 때마다 카운트를 증가시킵니다.
  count--;

  // 증가된 카운트를 표시합니다.
  clickCount.textContent = count;
});


// 리셋 버튼 클릭 이벤트에 대한 핸들러를 추가합니다.
resetButton.addEventListener('click', function() {
  // 카운트를 다시 0으로 설정합니다.
  count = 0;

  // 카운트를 표시합니다.
  clickCount.textContent = count;
});
