use std::collections::HashMap;

fn main() {
    let text = "Rust is fast. Rust is safe. Rust is also quite fun to learn and use!";
    
    let mut word_counts = HashMap::new();

    // Process the text
    for word in text.split_whitespace() {
        let cleaned_word = word
            .to_lowercase()
            .replace(".", "")
            .replace(",", "")
            .replace("!", "");

        // Skip empty strings
        if !cleaned_word.is_empty() {
            let count = word_counts.entry(cleaned_word).or_insert(0);
            *count += 1;
        }
    }

    // Sort the words alphabetically
    let mut sorted_words: Vec<_> = word_counts.iter().collect();
    sorted_words.sort_by(|a, b| a.0.cmp(b.0));

    // Display the results
    println!("Word Frequency Count:");
    println!("---------------------");
    for (word, count) in sorted_words {
        println!("{:<10} : {}", word, count);
    }
}
