fn check_palindrome(input: &String) -> bool {
    let half_length = input.len() / 2;
    input
        .chars()
        .take(half_length)
        .eq(input.chars().rev().take(half_length))
}

fn main() {
    let word = String::from("aabaa");
    let result = check_palindrome(&word);
    println!("Is {} a palindrome? {} ", word, result);
}
