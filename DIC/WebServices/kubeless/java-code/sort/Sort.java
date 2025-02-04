package io.kubeless;

import io.kubeless.Event;
import io.kubeless.Context;

import com.google.gson.JsonObject;
import java.util.Calendar;
import java.util.Arrays;

public class Sort {
    public static void sort1(int a[], int low, int hight) {
        int i, j, index;
        if (low > hight) {
            return;
        }
        i = low;
        j = hight;
        index = a[i];
        while (i < j) {
            while (i < j && a[j] >= index)
                j--;
            if (i < j)
                a[i++] = a[j];
            while (i < j && a[i] < index)
                i++;
            if (i < j)
                a[j--] = a[i];
        }
        a[i] = index;
        sort1(a, low, i - 1);
        sort1(a, i + 1, hight);
    }

    public static void quickSort(int a[]) {
        sort1(a, 0, a.length - 1);
    }

    public String foo(io.kubeless.Event event, io.kubeless.Context context) {
        long startTime = Calendar.getInstance().getTimeInMillis();

        String str;
        int[] arr;

        arr = new int[] {3, 6, 8, 10, 1, 2, 1, 4, 5, 6, 7, 8, 2232, 2, 4, 5, 7, 9, 20, 0, 88, 7, 34};
        quickSort(arr);

        JsonObject response = new JsonObject();
        response.addProperty("token", Arrays.toString(arr));
        response.addProperty("startTime",startTime);
        return response.toString();
    }
}