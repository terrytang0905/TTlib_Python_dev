package com.ttsoftware.utilities.algorithm.sorting;

import org.junit.runner.manipulation.Sorter;

/**
 * Interface for runners that allow sorting of tests. By sorting tests based on when they last failed, most recently
 * failed first, you can reduce the average time to the first test failing. Test sorting should not be used to
 * cope with order dependencies between tests. Tests that are isolated from each other are less
 * expensive to maintain and can be run individually.
 */
public interface Sortable {

	/**
	 * Sorts the tests using <code>sorter</code>
	 * @param sorter the {@link Sorter} to use for sorting the tests
	 */
	<T extends Comparable<T>> void sort(T[] array, boolean ascend);

}