from graph import graph

cv_text = open("cv.txt").read()
job_text = open("job.txt").read()

result = graph.invoke({
    "cv_text": cv_text,
    "job_text": job_text
})

print("\n=== RESULT ===")
print(result)
