function solution(n, words) {
  let tmp = words[0];
  let pastTmp = [tmp];

  for (let i = 1; i < words.length; i++) {
    let cur = words[i];

    if (cur[0] != tmp[tmp.length - 1] || pastTmp.includes(cur)) {
      return [(i % n) + 1, Math.floor(i / n) + 1];
    }

    pastTmp.push(cur);
    tmp = cur;
  }
  return [0, 0];
}

// 프로그래머스 2단계
