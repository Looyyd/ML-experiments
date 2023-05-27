import random
import os

def generate_new_samples(non_malicious_folder, malicious_folder, output_file):
    non_malicious_data = []
    malicious_data = []

    # Load non-malicious files
    for filename in os.listdir(non_malicious_folder):
        if filename.endswith('.txt'):
            with open(os.path.join(non_malicious_folder, filename), 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    non_malicious_data.append(line.strip())  # Mark as non-malicious

    # Load malicious files
    for filename in os.listdir(malicious_folder):
        if filename.endswith('.txt'):
            with open(os.path.join(malicious_folder, filename), 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    malicious_data.append(line.strip())  # Mark as malicious

    # Generate new samples
    new_samples = []
    for i in range(len(non_malicious_data)):
        non_malicious_msg = non_malicious_data[i]
        malicious_payload = random.choice(malicious_data)
        insert_position = random.randint(0, len(non_malicious_msg))
        new_msg = non_malicious_msg[:insert_position] + malicious_payload + non_malicious_msg[insert_position:]
        new_samples.append(new_msg)

    # Save new samples to file
    with open(output_file, 'w', encoding='utf-8') as f:
        for sample in new_samples:
            f.write(sample + '\n')

# Usage:
non_malicious_folder = 'non_payload_datasets'
malicious_folder = 'payload_datasets'
output_file = 'payload_datasets/messages_with_payloads.txt'
generate_new_samples(non_malicious_folder, malicious_folder, output_file)
