package ${packageName};

import com.shundaojia.ui.base.BaseActivity;

import javax.inject.Inject;

public class ${className}Activity extends BaseActivity implements ${className}MvpView {
    @Inject
    ${className}MainPresenter presenter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        activityComponent().inject(this);
        setContentView(R.layout.your_layout);
        presenter.attachView(this);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        presenter.detachView();
    }
}