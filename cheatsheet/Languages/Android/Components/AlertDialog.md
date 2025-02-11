
# Большая всплывашка
```java
import androidx.appcompat.app.AlertDialog;
```
```java
private void showAlert(String title, String text) {
    AlertDialog.Builder builder = new AlertDialog.Builder(MainActivity.this);
    builder.setTitle(title)
            .setMessage(text)
            .setCancelable(true) // Что можно скрыть
            .setPositiveButton("Закрыть приложение", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialogInterface, int i) {
                    finish();
                }
            })
            .setNegativeButton("Продолжить", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialogInterface, int i) {
                    dialogInterface.cancel(); // Закрыть Alert
                }
            })
    ;
    AlertDialog dialog = builder.create();
    dialog.show();
}```