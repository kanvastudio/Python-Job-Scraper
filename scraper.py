def save_results_to_md(job_list, filename="results.md"):
    """
    Takes a list of job dictionaries and writes them into a 
    clean, readable Markdown file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# 📋 Job Search Results\n\n")
        f.write(f"Total jobs found: {len(job_list)}\n\n")
        
        if not job_list:
            f.write("No jobs matched your criteria today.\n")
            return

        for job in job_list:
            title = job.get('title', 'N/A')
            company = job.get('company', {}).get('display_name', 'N/A')
            location = job.get('location', {}).get('display_name', 'N/A')
            link = job.get('redirect_url', '#')
            
            # Formatting as a Markdown list item
            f.write(f"### {title}\n")
            f.write(f"- **Company:** {company}\n")
            f.write(f"- **Location:** {location}\n")
            f.write(f"- [View Job Posting]({link})\n\n")
            f.write("---\n\n")
            
    print(f"✅ Success! Results saved to {filename}")

# 1. Fetch the data
raw_jobs = fetch_jobs(APP_ID, APP_KEY)

# 2. Filter the data (using your CS61A HOF skills)
is_remote = lambda j: "remote" in j.get('description', '').lower()
filtered_jobs = filter_jobs(raw_jobs, is_remote)

# 3. Save the data to a file
save_results_to_md(filtered_jobs)
