function solution(arr) {
  // 두 수의 최소공배수를 계산하는 함수
  function findLCM(a, b) {
    // 최대공약수를 구하는 함수
    function findGCD(x, y) {
      if (y === 0) {
        return x;
      } else {
        return findGCD(y, x % y);
      }
    }

    // 최소공배수 계산
    const gcd = findGCD(a, b);
    const lcm = (a * b) / gcd;

    return lcm;
  }

  // 배열의 수들의 최소공배수 계산
  let lcm = arr[0];
  for (let i = 1; i < arr.length; i++) {
    lcm = findLCM(lcm, arr[i]);
  }

  return lcm;
}
