# Installation

This project uses a Conda environment to install Python and all required packages.

## Prerequisites

Before starting, install:

- [Miniconda](https://www.anaconda.com/download/success) or [Anaconda](https://www.anaconda.com/download/success) 
- Python `>=3.7` and `<3.13`

> Note: If you install Anaconda or Miniconda, you do not need to install Python separately. Conda will create the correct Python version for this tutorial.

---

## Downloading the tutorial files

The tutorial files are available on GitHub:

```text
https://github.com/nicola-wiseman/Abil_tutorial
```

You can download them in one of two ways.

### Option 1: Download as a ZIP file

This is the easiest option if you are new to GitHub or the terminal.

1. Open this page in your web browser:

   ```text
   https://github.com/nicola-wiseman/Abil_tutorial
   ```

2. Click the green **Code** button.

3. Click **Download ZIP**.

4. After the ZIP file downloads, unzip it.

   - On macOS, double-click the ZIP file.
   - On Windows, right-click the ZIP file and select **Extract All...**.

5. Open the extracted folder.

The extracted folder is the example folder. The `environment.yml` file should be in the root of this folder.

### Option 2: Download using Git

Use this option if you already have Git installed.

Open a terminal and run:

```sh
git clone https://github.com/nicola-wiseman/Abil_tutorial.git
```

Then move into the downloaded folder:

```sh
cd Abil_tutorial
```

The `environment.yml` file should be in this folder.

> If you do not have Git installed, use **Option 1: Download as a ZIP file**.

---

## Installing the tutorial environment

The file `environment.yml` is located in the root of this example folder.  
Before running the installation command, open a terminal and move into that folder.

### Step 1: Open a terminal

#### On macOS

Open **Terminal**:

1. Press `Cmd + Space`
2. Type `Terminal`
3. Press `Enter`

#### On Windows

Open **Anaconda Prompt**:

1. Open the Start menu
2. Search for `Anaconda Prompt`
3. Click to open it

> On Windows, use **Anaconda Prompt** rather than Command Prompt or PowerShell unless you have already configured Conda for those terminals.

---

### Step 2: Move into the example folder

Use the `cd` command to move into the folder that contains `environment.yml`.

For example, on macOS or Windows:

```sh
cd path/to/Abil_tutorial
```

Replace `path/to/Abil_tutorial` with the actual path on your computer.

For example:

```sh
cd Downloads/Abil_tutorial
```

If the folder path contains spaces, wrap it in quotes:

```sh
cd "Downloads/another folder/Abil_tutorial"
```

You can check that you are in the correct folder by listing the files.

On macOS:

```sh
ls
```

On Windows Anaconda Prompt:

```sh
dir
```

You should see:

```sh
environment.yml
```

---

### Step 3: Create the Conda environment

From the root of the example folder, run:

```sh
conda env create -f environment.yml
```

This may take several minutes.

---

### Step 4: Activate the environment

After the environment has been created, activate it with:

```sh
conda activate abil-tutorial-env
```

You should now see the environment name at the beginning of your terminal prompt, for example:

```sh
(abil-tutorial-env)
```

---

### Step 5: Confirm the installation

Check that Python is available inside the environment:

```sh
python --version
```

You can also check that Conda is using the correct environment:

```sh
conda info --envs
```

The active environment should have an asterisk `*` next to it.

---

## Updating the environment

If `environment.yml` changes later, update the environment from the root of the example folder with:

```sh
conda env update -f environment.yml --prune
```

Then reactivate the environment:

```sh
conda activate abil-tutorial-env
```