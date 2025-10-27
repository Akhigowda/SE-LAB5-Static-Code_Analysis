# Issues Identified and Fixes – Lab 5: Static Code Analysis

| **Tool** | **Issue Type / Code** | **Line(s)** | **Description of Issue** | **Severity** | **Fix Implemented** |
|-----------|-----------------------|--------------|---------------------------|---------------|----------------------|
| **Pylint** | `W0102` – Mutable default argument | 14 | Function `add_item` used `logs=[]` as default parameter, which is shared across function calls | Medium | Changed default to `logs=None` and initialized a new list inside the function |
| **Pylint** | `W0702` – Broad `except:` | 26 | The `remove_item()` function used a generic `except:` block, hiding specific errors | High | Replaced with `except KeyError:` to catch specific missing-key errors |
| **Bandit** | `B307` – Use of `eval()` | 72 (old version) | Code executed `eval("print('eval used')")`, which allows arbitrary code execution | High | Removed `eval()` completely since it was unnecessary |
| **Pylint / Logic** | Type validation missing | 18 | Invalid data types like `(123, "ten")` caused logic errors when adding items | Medium | Added input type checking (`isinstance(item, str)` and `isinstance(qty, (int, float))`) |
| **Pylint** | `W0603` – Use of global statement | 64 | The `global` keyword was used to modify global variable state directly | Low | Replaced with safe `STOCK_DATA.update()` call in `main()` instead of modifying globals |
| **Flake8** | `E501` – Line too long (>79 chars) | 12, 24, 56 | Several lines exceeded PEP8’s recommended line length | Low | Reformatted long lines using multi-line logging calls and argument wrapping |
| **Pylint** | `C0114` – Missing module docstring | 1 | File lacked a proper module-level docstring | Low | Added a descriptive docstring at the top of the file |
| **Bandit** | `B110` – Insecure file handling | 46, 58 | Files were opened without `with` statement context management | Medium | Replaced raw `open()`/`close()` calls with `with open(...)` blocks |
| **Flake8 / PEP8** | Formatting and indentation inconsistencies | Various | Minor style inconsistencies like extra spaces or indentation depth | Low | Reformatted code according to PEP8 guidelines using manual adjustments |

---

### ✅ Summary of Fixes Applied
- Replaced unsafe or bad practices (`eval`, `except:`).
- Added strict type validation and logging.
- Improved readability and maintainability.
- Ensured PEP8 and security compliance.
- Verified all fixes using **Pylint**, **Flake8**, and **Bandit**.

**Final Results:**
- **Pylint Score:** 10.00 / 10  
- **Flake8:** No violations  
- **Bandit:** No security issues
