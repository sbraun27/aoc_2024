fn is_safe(line: Vec<i32>) -> bool {
    let first_diff: Vec<i32> = line[1..]
        .iter()
        .zip(line[..line.len() - 1].iter())
        .map(|(current, previous)| current - previous)
        .collect();

    first_diff
        .iter()
        .all(|&diff| diff.abs() <= 3) && (
            first_diff.iter().all(|&diff| diff > 0) || 
            first_diff.iter().all(|&diff| diff < 0)
        )
}

fn is_safe_part_2(line: Vec<i32>) -> bool {
    for i in 0..line.len() {
        let mut new_nums = line.clone();
        new_nums.remove(i);
        if is_safe(new_nums) {
        return true;
        }
    };
    false
}

fn main() {
    let input = include_str!("input.txt");

    let reports = input
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|num| num.parse::<i32>().expect("Invalid Number"))
                .collect::<Vec<i32>>()
        })
        .collect::<Vec<Vec<i32>>>();

    let part_1 = reports
        .iter()
        .filter(|&vec| is_safe(vec.to_vec()))
        .count();

    let part_2 = reports
        .iter()
        .filter(|&vec| is_safe_part_2(vec.to_vec()))
        .count();

    println!("Number of safe lines (Part 1): {}", part_1);
    println!("Number of safe lines (Part 2): {}", part_2);
}