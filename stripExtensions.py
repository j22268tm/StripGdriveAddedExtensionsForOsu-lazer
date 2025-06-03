import os

def rename_files_remove_extension(directory_path, dry_run=True):
    prospective_rename_count = 0
    actual_renamed_count = 0
    skipped_count = 0
    error_count = 0
    log_messages = []

    if not os.path.isdir(directory_path):
        log_messages.append(f"Error: Directory '{directory_path}' not found.")
        return prospective_rename_count, actual_renamed_count, skipped_count, error_count, log_messages

    for root, _, files in os.walk(directory_path):
        for filename in files:
            base_name, extension = os.path.splitext(filename)
            
            if extension:
                old_filepath = os.path.join(root, filename)
                new_filename = base_name 
                new_filepath = os.path.join(root, new_filename)
                
                if old_filepath == new_filepath: 
                    continue
                
                current_log_base = f"'{old_filepath}' -> '{new_filepath}'"

                if os.path.exists(new_filepath):
                    log_messages.append(f"Skipped: {current_log_base} (Reason: Target exists)")
                    skipped_count += 1
                    continue
                
                prospective_rename_count +=1
                
                if dry_run:
                    log_messages.append(f"To be renamed: {current_log_base}")
                else:
                    try:
                        os.rename(old_filepath, new_filepath)
                        log_messages.append(f"Success: {current_log_base}")
                        actual_renamed_count += 1
                    except OSError as e:
                        log_messages.append(f"Error: {current_log_base} (Reason: {e})")
                        error_count += 1
            
    return prospective_rename_count, actual_renamed_count, skipped_count, error_count, log_messages

if __name__ == "__main__":
    print("--------------------------------------------------------------------")
    print(" osu!lazer 'files' Directory Extension Removal Script")
    print("--------------------------------------------------------------------")
    print("Removes extensions from all files in specified directory/subdirectories")
    print("Example: 'c1a89f.mp3' becomes 'c1a89f'")
    print("\n!!! WARNING !!!")
    print("This operation permanently modifies filenames. Backup your directory first.")
    print("Selecting wrong directory may cause serious issues.")
    print("--------------------------------------------------------------------")

    target_dir_input_raw = ""
    while not target_dir_input_raw:
        target_dir_input_raw = input("Enter full path to target directory\n(Example: C:\\Users\\You\\AppData\\Roaming\\osulazer\\files or /path/to/osulazer/files): ").strip()
        if not target_dir_input_raw:
            print("No path entered. Please try again.")

    if target_dir_input_raw.startswith('"') and target_dir_input_raw.endswith('"'):
        target_dir = target_dir_input_raw[1:-1]
    else:
        target_dir = target_dir_input_raw

    if not os.path.isdir(target_dir):
        print(f"\nError: Path '{target_dir}' is not a valid directory.")
        print("Verify path and restart script.")
    else:
        print(f"\nTarget directory: '{target_dir}'")
        
        dry_run_choice = input("Run dry-run first? (Shows changes without modifying) (yes/no) [yes]: ").strip().lower()
        is_dry_run = (dry_run_choice != 'no')

        if is_dry_run:
            print("\nStarting [DRY-RUN MODE]...")
        else:
            print("\n[LIVE MODE] selected.")
            confirm_action = input(f"WARNING: Files in '{target_dir}' will be permanently renamed.\n"
                                   "This cannot be undone. Type 'yes' to proceed: ").strip()
            if confirm_action != 'yes':
                print("Operation cancelled.")
                exit()
            print("\nStarting live execution...")

        p_count, a_count, s_count, e_count, logs = rename_files_remove_extension(target_dir, dry_run=is_dry_run)
        
        print("\n--- Processing Log ---")
        if not logs:
            if os.path.isdir(target_dir):
                 print("No files with extensions found.")
        else:
            for log_entry in logs:
                print(log_entry)
        print("--- End Log ---")

        print("\n--- Summary ---")
        if is_dry_run:
            print(f"Mode: Dry-run")
            print(f"Files to rename: {p_count}")
            print(f"Skipped files (target exists): {s_count}")
            if p_count > 0:
                 print("\nReview log and run again without dry-run to apply changes.")
            elif os.path.isdir(target_dir):
                print("No files with extensions found.")

        else:
            print(f"Mode: Live execution")
            print(f"Successfully renamed: {a_count}")
            print(f"Skipped files (target exists): {s_count}")
            print(f"Errors encountered: {e_count}")
            if e_count > 0:
                print("Check logs for error details.")
            print("Operation completed.")
