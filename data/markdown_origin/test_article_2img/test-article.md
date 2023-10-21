![](./.img/img-test.png)

# TEST ARTICLE

This is the basic syntax, but it is not the best practice. If the file is not found, it will generate a FileNotFound Error.

## 222

You can handle this by encasing the delete statement in an if-else block. Let’s look at it below:

```
if os.path.isfile(<filename or file path>):
    os.remove(<filename>)
else:
    print('The file does not exist.')
```

### exist

The if-else block first checks if the file exists in the file system with the os.path.isfile() method before trying to delete it. If the file exists, it deletes it.

>The if-else block first checks if the file exists in the file system with the os.path.isfile() method before trying to delete it. If the file exists, it deletes it.

If it doesn’t, it returns a print statement instead of an error.

---

In this section, we’ll discuss how to work with different file types in Python, specifically focusing on binary files and CSV files. We’ll cover how to read and write data using these file types.