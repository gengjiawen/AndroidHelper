package ${packageName};

import com.shundaojia.ui.base.BasePresenter;

import javax.inject.Inject;

public class ${className}Presenter extends BasePresenter<${className}MvpView> {

    @Inject
    public ${className}Presenter() {
    }

    @Override
    public void attachView(${className}MvpView mvpView) {
        super.attachView(mvpView);
    }

    @Override
    public void detachView() {
        super.detachView();
    }
}