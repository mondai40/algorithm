function either24(nums: number[]):boolean{
  return either24Helper(nums, 0, false, false);
}
function either24Helper(nums: number[], index: number, twoTwo: boolean, twoFour: boolean): boolean {
  if (index > nums.length) return ( twoTwo && !twoFour ) || ( !twoTwo && twoFour );
  if (nums[index] === 2 && nums[index + 1] === 2) {
    twoTwo = true;
  } else if (nums[index] === 4 && nums[index + 1] === 4) {
    twoFour = true;
  }
  return either24Helper(nums, ++index, twoTwo, twoFour);
}